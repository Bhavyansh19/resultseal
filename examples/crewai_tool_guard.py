"""Guard a CrewAI tool result before it can propagate to sibling agents.

Install ``crewai`` to run the complete example.  In multi-agent crews, one
agent's tool output is often handed to sibling agents through shared task
context.  Blocking an unverified result at the tool boundary keeps empty lists
and partial mutations from cascading into hallucinations across the crew.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from resultseal.contracts import load_contract_file
from resultseal.limits import Limits
from resultseal.models import Decision
from resultseal.normalize import normalize
from resultseal.rules import ReferenceClock, evaluate

CONTRACT_PATH = Path(__file__).with_name("customer_contract.json")


class BlockedObservation(RuntimeError):
    """Raised when ResultSeal blocks an unsafe tool observation."""


def guard_search_result(result: object) -> object:
    """Return a verified result or block the tool observation."""
    clock = ReferenceClock(now=datetime.now(UTC))
    contract = load_contract_file(CONTRACT_PATH, Limits())

    normalization = normalize(
        {
            "kind": "json",
            "source_ref": "mcp://crm-server",
            "target_ref": "customer:42",
            "tool_name": "search_customer",
            "body": result,
        },
        clock,
    )

    evaluation = evaluate(
        normalization.envelope,
        normalization.payload,
        contract,
        clock,
    )

    if evaluation.decision is not Decision.SEALED:
        codes = ", ".join(evaluation.reason_codes)
        raise BlockedObservation(
            f"ResultSeal blocked the tool observation: {codes}"
        )

    return normalization.payload


def build_tool():  # type annotations would require an optional dependency
    """Create a CrewAI tool with a guarded result."""
    from crewai.tools import tool

    @tool("Search Customer")
    def search_customer(query: str) -> object:
        """Search the customer database."""
        # Stand-in for a database call. Raising here prevents [] from becoming
        # a verified observation that sibling agents would treat as ground truth.
        database_result: list[object] = []
        return guard_search_result(database_result)

    return search_customer


if __name__ == "__main__":
    search_customer = build_tool()

    try:
        search_customer.run(query="customer 42")
    except BlockedObservation as exc:
        print(f"Successfully blocked unverified observation: {exc}")
