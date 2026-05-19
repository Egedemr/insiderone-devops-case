from fastapi.testclient import TestClient


def test_version_falls_back_to_local_dev(client: TestClient) -> None:
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "local-dev"}


def test_version_uses_env_var(client: TestClient, monkeypatch) -> None:
    monkeypatch.setenv("APP_VERSION", "1.2.3-build.7")
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.2.3-build.7"}
