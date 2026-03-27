AUTH_FILE="auth.log"
def read_auth_log()->list[str]:
    with open("auth.log") as out_data_about_attempts:
        data = out_data_about_attempts.readlines()
    return data