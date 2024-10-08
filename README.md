[![CI](https://github.com/infrasonar/paloalto-probe/workflows/CI/badge.svg)](https://github.com/infrasonar/paloalto-probe/actions)
[![Release Version](https://img.shields.io/github/release/infrasonar/paloalto-probe)](https://github.com/infrasonar/paloalto-probe/releases)

# InfraSonar PaloAlto Probe

Documentation: https://docs.infrasonar.com/collectors/probes/paloalto/
## Environment variable

Variable            | Default                        | Description
------------------- | ------------------------------ | ------------
`AGENTCORE_HOST`    | `127.0.0.1`                    | Hostname or Ip address of the AgentCore.
`AGENTCORE_PORT`    | `8750`                         | AgentCore port to connect to.
`INFRASONAR_CONF`   | `/data/config/infrasonar.yaml` | File with probe and asset configuration like credentials.
`MAX_PACKAGE_SIZE`  | `500`                          | Maximum package size in kilobytes _(1..2000)_.
`MAX_CHECK_TIMEOUT` | `300`                          | Check time-out is 80% of the interval time with `MAX_CHECK_TIMEOUT` in seconds as absolute maximum.
`DRY_RUN`           | _none_                         | Do not run demonized, just return checks and assets specified in the given yaml _(see the [Dry run section](#dry-run) below)_.
`LOG_LEVEL`         | `warning`                      | Log level (`debug`, `info`, `warning`, `error` or `critical`).
`LOG_COLORIZED`     | `0`                            | Log using colors (`0`=disabled, `1`=enabled).
`LOG_FMT`           | `%y%m%d %H:%M:%S`              | Log format prefix.

## API key
This probe requires an [API key](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/get-your-api-key) which must be placed in the `INFRASONAR_CONF` configuration file. For example:

```yaml
paloalto:
  config:
    secret: 'gJlQWE56987nBxIqyfa62sZeRtYuIo2BgzEA9UOnlZBhU=='
```

## Docker build

```
docker build -t paloalto-probe . --no-cache
```

## Dry run

Available checks:
- `interface`
- `route`
- `session`
- `system`

Create a yaml file, for example _(test.yaml)_:

```yaml
asset:
  name: "foo.local"
  check: "system"
  config:
    address: "192.168.1.2"
```

Run the probe with the `DRY_RUN` environment variable set the the yaml file above.

```
DRY_RUN=test.yaml python main.py
```
