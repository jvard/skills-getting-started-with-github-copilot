def test_get_activities_returns_dictionary_payload(client):
    # Arrange
    expected_status_code = 200

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == expected_status_code
    assert isinstance(payload, dict)
    assert len(payload) > 0


def test_get_activities_contains_expected_structure(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in payload

    for details in payload.values():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
