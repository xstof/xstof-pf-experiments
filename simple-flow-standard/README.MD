# Simple flow - Standard

## Run with data

To create a run that tests this flow with the data items in `test-data-colours.jsonl` execute the following command:

```sh
pf run create --flow . --name myrun --data ../test-data-colours.jsonl --column-mapping colour='${data.colour}'
```

You may want to visualize the results later (does not work in dev container):

```sh
pf run visualize -n myrun
```

Alternative you can get the detailed results for every data-line in text-form:

```sh
pf run show-details -n myrun
```