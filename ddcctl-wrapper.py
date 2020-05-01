import yaml
import subprocess
import re

def run_command(args):
    cp = subprocess.run(args, capture_output=True)
    return cp.stdout.decode('utf-8')


def extract(pattern, string):
    return re.search(pattern, string).groups()[0]


def display_setting(config, mode, display_key, display_num):
    display_config = config[mode][display_key]
    if 'brightness' in display_config:
        print('{} > brightness => {}'.format(display_key, display_config['brightness']))
        run_command(['ddcctl', '-d', str(display_num), '-b', str(display_config['brightness'])])
    if 'contrast' in display_config:
        print('{} > contrast => {}'.format(display_key, display_config['contrast']))
        run_command(['ddcctl', '-d', str(display_num), '-c', str(display_config['contrast'])])


def aparse():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', default='ddcctl-config.yml',
        help='path to config yaml file'
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-m', '--mode'
    )
    group.add_argument(
        '-l', '--list', action='store_true',
        help='print external displays list'
    )
    return parser.parse_args()


def main():
    args = aparse()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    num_displays = int(extract('found (\d) external displays', run_command(['ddcctl'])))

    for i in range(1, num_displays + 1):
        stdout = run_command(['ddcctl', '-d', str(i)])
        edid_serial = extract('I: got edid.serial: ([^\n]*)\n', stdout)
        edid_name = extract('I: got edid.name: ([^\n]*)\n', stdout)

        if args.list:
            print('#{}: serial = "{}", name = "{}"'.format(i, edid_serial, edid_name))
            
        else:
            if edid_serial in config[args.mode]:
                display_setting(config, args.mode, edid_serial, i)
            elif edid_name in config[args.mode]:
                display_setting(config, args.mode, edid_name, i)


if __name__ == "__main__":
    main()
