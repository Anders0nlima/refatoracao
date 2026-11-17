from refatoracao.q8.student_registration import Address, ContactInfo, StudentRegistration


def test_validity_examples():
    ok = StudentRegistration("Juremilda", "n@x.com", "9199999999", "Belém", "66000-000")
    assert ok.is_valid()

    bad_zip = StudentRegistration("Juremilda", "n@x.com", "9199999999", "Belém", "66000000")
    assert not bad_zip.is_valid()


def test_formatted_contact_example():
    s = StudentRegistration("Max", "v@ufpa.br", "91988887777", "Belém", "66000-000")
    assert s.formatted_contact() == "Max | v@ufpa.br | 91988887777 | Belém - 66000-000"


def test_refactor_goal_extract_class_contact_and_address():
    # TODO: extrair ContactInfo/Address e mover validações/format mantendo testes.
    address = Address("Belém", "66000-000")
    assert address.is_valid()
    assert address.format() == "Belém - 66000-000"
    bad_address = Address("Belém", "123")
    assert not bad_address.is_valid()
    contact = ContactInfo("aluno@ufpa.br", "91999998888")
    assert contact.is_valid()
    assert contact.format() == "aluno@ufpa.br | 91999998888"
    bad_contact = ContactInfo("sem-arroba", "123")
    assert not bad_contact.is_valid()
