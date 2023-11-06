# Simple Flow

This simple flow merely demonstrates how a flow with a single LLM node looks like.

## Login

To use the flow, make sure to either configure the right connections first or to use the connections as configured in your Azure Prompt flow environment.  To avoid having to log in every time you run the flow, log into the azure cli first:

```sh
az login
az account show
```

Then, when not correct, choose your subscription:

```sh
az account set -s [your-subscription-id]
```

## Test the flow

To test the flow:

```sh
cd simple-flow-chat/simple-flow-chat
pf flow test --flow .
```

Besides in the VS Code Prompt flow user interface, in the `.promptflow` directory, the `flow.detail.json` will contain the details of the test run.  Because this is test run, the run results are not remembered:

```sh
pf run list
```

shows `[]`

## Run the flow in batch

We'll give our run an explicit name: `my-first-run` so we can easily refer to it later on.

```sh
pf run create --flow . --name my-first-run --data ../test-data.jsonl --column-mapping input.chat_input='${data.question}'
```



