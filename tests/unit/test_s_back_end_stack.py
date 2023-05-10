import aws_cdk as core
import aws_cdk.assertions as assertions

from s_back_end.s_back_end_stack import SBackEndStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s_back_end/s_back_end_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SBackEndStack(app, "s-back-end")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
