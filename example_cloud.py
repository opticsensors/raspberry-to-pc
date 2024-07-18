import cloud

remote_name = 'first_remote'
remote_type = 'drive'
in_path = 'results'
out_path = f'{remote_name}:Eurecat'
list_of_remotes = cloud.list_remotes()

if list_of_remotes:
    for e in list_of_remotes:
        cloud.delete_remote(e)

cloud.create_remote(remote_name, remote_type)
# refresh_remote(remote_name)
cloud.copy_to_remote(in_path, out_path)
