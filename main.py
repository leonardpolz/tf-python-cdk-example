#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.azurerm.provider import AzurermProvider, AzurermProviderFeatures
from imports.azurerm.resource_group import ResourceGroup

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AzurermProvider(self, "AzureRM", 
            features=[AzurermProviderFeatures()],
            subscription_id="2c3936dd-ba68-4d31-8975-e4d1cc9fe53f"
        )

        rg = ResourceGroup(
            self,
            "exampleResourceGroup",
            name="cdktf-example-rg",
            location="eastus"
        )

app = App()
MyStack(app, "tf-python-cdk-example")
app.synth()