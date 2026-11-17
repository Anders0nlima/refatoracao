from refatoracao.q5.password_reset_notification import PasswordResetNotification


def test_render_should_contain_subject_and_body():
    n = PasswordResetNotification("Joelma")
    r = n.render()

    assert "Redefinição de senha" in r
    assert "Olá Joelma" in r


def test_refactor_goal_collapse_hierarchy_remove_redundant_subclass():
    # TODO: após refatorar, VIPPasswordResetNotification deve deixar de existir (ou ganhar comportamento real).
    # O comportamento de renderização deve permanecer.
    n = PasswordResetNotification("Chimbinha")
    r = n.render()

    assert "Redefinição de senha" in r
    assert "Olá Chimbinha, clique no link para redefinir." in r
