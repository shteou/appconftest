# appconftest

appconftest is a PoC which provides a wrapper around `conftest` which aims to
allow applications with multiple configuration sources to be easily tested
with `conftest`

## Configuration files / policies

```
 .----------------------------------------------------------------.
| configuration file(s) | policies      | notes                    |
| --------------------- | ------------- | ------------------------ |
| charts/your-app/      | charts        | helm template pre-render |
| Dockerfile            | dockerfile    |                          |
```

## Usage

```
./build.sh
cd my-service
docker run -it --rm -v `pwd`:/appconftest/source appconftest
```

## Future work

The goal is to make this more extensible to different types of configuration
test. e.g. by specifying in yaml, or on the commandline, the configuration file /
policy pairs to execute.

It will likely also add conventions to conftest policies (e.g. ensuring all policies
contain links with further information), and provide better output (e.g. aggregation
of multiple conftest runs into both human and machine-readable formats).
