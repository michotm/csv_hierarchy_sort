import click
import csv


def compute_complete_path(indexed_csv, current_id, complete_path, parent_id_key='parent_id'):
    if current_id in indexed_csv and indexed_csv[current_id][parent_id_key]:
        return compute_complete_path(indexed_csv, indexed_csv[current_id][parent_id_key], f"{indexed_csv[current_id][parent_id_key]}/{complete_path}", parent_id_key)
    else:
        return f"{complete_path}"


@click.command()
@click.option('--input_file', help='Input csv file')
@click.option('--output_file', help='Output csv file')
@click.option('--id_key', default='id', help='name of id col')
@click.option('--parent_id_key', default='parent_id', help='name of parent_id col')
@click.option('--delimiter', default=';', help='CSV delimiter')
def main(id_key, parent_id_key, input_file, output_file, delimiter):
    with open(input_file) as fin:
        reader = csv.DictReader(fin, delimiter=delimiter)
        indexed_csv = {r[id_key]: r for r in reader}
        fieldnames = [k for k in next(iter(indexed_csv.values()))]

    for r in indexed_csv:
        if indexed_csv[r][parent_id_key] in indexed_csv:
            indexed_csv[r]['complete_path'] = compute_complete_path(
                indexed_csv, r, r, parent_id_key)
        else:
            indexed_csv[r]['complete_path'] = r
            
    l = [indexed_csv[r]['complete_path'].split(
        '/') for r in indexed_csv if indexed_csv[r]['complete_path'] != '']
    levels = {}
    for s in range(1, max([len(r) for r in l]) + 1):
        levels[s] = list(set([r[s - 1] for r in l if len(r) >= s]))

    res = []
    ids = []
    with open(output_file, 'w') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        for level in levels:
            for id in levels[level]:
                if id not in ids:
                    indexed_csv[id].pop('complete_path')
                    writer.writerow(indexed_csv[id])
                    ids.append(id)


if __name__ == "__main__":
    main()
