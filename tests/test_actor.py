from src.actor import Actor

def test_csv_lookup_found():
    actor = Actor()
    result = actor.run_tool("csv_lookup", "price of item_5")
    assert "item_5" in result
    assert "costs" in result

def test_csv_lookup_not_found():
    actor = Actor()
    result = actor.run_tool("csv_lookup", "price of unknown_item")
    assert "not found" in result.lower()
