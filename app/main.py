import click
from .scripts import get_files, validate_input
from .DataEngine import DataEngine

files = get_files()
engine = DataEngine(files)


@click.command()
@click.option('--incorrect-emails', '-ic', is_flag=True, default=False,
              help='Prints the number of invalid emails, then one invalid email per line.')
@click.option('--search', '-s', type=str, default=None,
              help='Takes a string argument and print the number of found emails, then one found email per line.')
@click.option('--group-by-domain', '-gbd', is_flag=True, default=False,
              help='Groups emails by one domain and order domains and emails alphabetically')
@click.option('--find-emails-not-in-logs', '-feil', type=str, default=None,
              help='Prints the numbers of found emails in logs, then one found email per line sorted alphabetically.')
@click.option('--remove-dupes', '-rd', is_flag=True, default=False,
              help='Removes dupes from the data set, optional')
def cli(incorrect_emails, search, group_by_domain, find_emails_not_in_logs, remove_dupes):
    var_dict = {'remove_dupes': remove_dupes,
                'incorrect_emails': incorrect_emails,
                'search': search,
                'group_by_domain': group_by_domain,
                'find_emails_not_in_logs': find_emails_not_in_logs}
    validate_input(var_dict)

    if remove_dupes:
        engine.remove_dupes()

    if incorrect_emails:
        engine.print_incorrect()

    elif search:
        engine.search(search)

    elif group_by_domain:
        engine.group_by_domain()

    elif find_emails_not_in_logs:
        engine.read_logs(find_emails_not_in_logs)

    else:
        engine.print_data()


if __name__ == '__main__':
    cli()


