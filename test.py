from checkout import checkout, get_token, get_user
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

# тест только для ОС Linux
def test_step1():
    result = checkout(f"nikto -h {data['address']} -ssl -Tuning 4", "0 error(s)")
    assert result

def test_step2():
    assert get_user(get_token(), '23573') == 'Alex'
