from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='TODO_API',
    settings_file=['api/configs/settings.toml', 'api/configs/.secrets.toml'],
    environment=True
)
