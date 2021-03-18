import generators
import queries
import logics

# logics.simple_logic(
#     login_generator=generators.ListGenerator(tokens=['admin', 'jack', 'cat']),
#     password_generator=generators.FileGenerator(filename='pop_passwords.txt'),
#     query=queries.local_server
# )

# logics.get_accounts_logic(
#     login_generator=generators.FileGenerator(filename='pop_passwords.txt'),
#     password_generator=generators.FileGenerator(filename='pop_passwords.txt'),
#     query=queries.local_server
# )

logics.get_accounts_logic(
    login_generator=generators.ListGenerator(tokens=['admin', 'jack', 'cat']),
    password_generator=generators.BruteForceGenerator(),
    query=queries.local_server,
    password_limit=1000000
)

# logics.get_password_logic(
#     login_generator=generators.ListGenerator(tokens=['admin', 'jack', 'cat']),
#     password_generator=generators.FileGenerator(filename='pop_passwords.txt'),
#     query=queries.local_server_protected
# )
