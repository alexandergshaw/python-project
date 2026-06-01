from app import app


def test_core_routes_render_successfully():
    client = app.test_client()
    for route in ['/', '/portfolio', '/assignments', '/skills', '/reports']:
        response = client.get(route)
        assert response.status_code == 200
