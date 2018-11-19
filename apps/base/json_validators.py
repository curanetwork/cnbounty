import voluptuous as v


fields = v.Schema([{
    'name': str,
    'type': v.Any(
        'url', 'short_text', 'long_text', 'number', 'boolean', 'enum'),
    v.Optional('required', True): bool,
    v.Optional('min_length'): int,
    v.Optional('max_length'): int,
    v.Optional('min_digit'): v.Coerce(float),
    v.Optional('max_digit'): v.Coerce(float),
    v.Optional('choices'): [str]
}], required=True)


details = v.Schema({
    'field_name': str,
    'type': v.Any(
        'url', 'short_text', 'long_text', 'number', 'boolean', 'enum'),
    'value': v.Any(int, str, bool, v.Url())
}, required=True)
