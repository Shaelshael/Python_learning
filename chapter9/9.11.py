from user_info import User, Admin, Privileges

admen = Admin('ivan', 'ivanov', '33', 'russia')
admen.describe_user()
admen.privileges.show_privileges()
