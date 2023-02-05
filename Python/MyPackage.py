from rv import commands, rvtypes
from rv.commands import NeutralMenuState

class Example_Package_MyStuffMode(rvtypes.MinorMode):

    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        globalBindings = None #[("Event-Name", self.eventCallback, "DescriptionOfBinding")]
        localBindings = None

        menu = [
            ("Example", [
                    ("Run Example", self.runExample, None, lambda: NeutralMenuState),
            ])
        ]

        self.init("Example_Package_MyStuff", globalBindings, localBindings, menu)

    def runExample(self, event):
        print("DEBUG: Example Ran.")

def createMode():
    return Example_Package_MyStuffMode()