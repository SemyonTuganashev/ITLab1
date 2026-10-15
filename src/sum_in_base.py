def add_in_base(a: str, b: str, base: int) -> str:
    python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat
    """
    Складывает два числа, записанных в системе счисления с основанием base.

    :param a: первое число, строка (например, "1011")
    :param b: второе число, строка (например, "111")
    :param base: основание системы счисления, 2 <= base <= 36
    :return: сумма в той же системе счисления, строка

    Пример:
        add_in_base("1011", "111", 2) -> "10010"
        add_in_base("FF", "1", 16) -> "100"
    """
    raise NotImplementedError("Реализуйте функцию add_in_base")
