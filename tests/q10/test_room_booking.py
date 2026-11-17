import pytest

from refatoracao.q10.room_booking import BookingRequest, RoomBooking


def test_quote_examples():
    rb = RoomBooking()

    req1 = BookingRequest("B", 1, "101", 8, 10, False, False, 10)
    assert rb.quote(req1) == pytest.approx(100.0, abs=0.001)

    req2 = BookingRequest("A", 3, "101", 8, 10, True, True, 50)
    assert rb.quote(req2) == pytest.approx(
        (2 * 50.0 + 30 + 20) * 1.15 + 10, abs=0.01
    )
    
    req3 = BookingRequest("B", 1, "LAB", 8, 10, False, False, 10)
    assert rb.quote(req3) == pytest.approx(
        (2 * 50.0) + 40, abs=0.01
    )


def test_refactor_goal_introduce_parameter_object():
    # TODO: introduzir BookingRequest/Room/Schedule e reduzir parâmetros primitivos.
    # Ajuste as chamadas acima se necessário, mantendo os valores esperados.
    rb = RoomBooking()
    
    req = BookingRequest(
        building="A",
        floor=4,
        room="LAB",
        start_hour=14,
        end_hour=17,
        projector=True,
        sound=True,
        attendees=45,
    )
    
    assert rb.quote(req) == 280.0
    assert req.duration_hours == 3
