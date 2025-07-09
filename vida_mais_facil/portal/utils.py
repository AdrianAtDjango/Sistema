from .models import User

def autentica_manual(cpf, password):
    try:
        user = User.objects.get(cpf=cpf)
        if user.check_password(password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None