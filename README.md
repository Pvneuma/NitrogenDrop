# NitrogenDrop

## Config

You need to create a configuration file named `config.yml` in root directory.

Here is a template of  :

```
server:
    host: 0.0.0.0
    port: 8181
    workers: 1 # the number of worker processes

size: 1024*1024*10 # the number of bytes that the server reads from the temporary file each time

directory: ./downloads/ # the directory to store the downloaded files

base_url: http://127.0.0.1:8181 # Your server ip
```

