from rv import commands, rvtypes
from rv.commands import NeutralMenuState

class Example(rvtypes.MinorMode):

    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        globalBindings = None #[("Event-Name", self.eventCallback, "DescriptionOfBinding")]
        localBindings = None

        menu = [
            ("jonsor", [
                    ("Run Example", self.runExample, None, lambda: NeutralMenuState),
            ])
        ]

        self.init("Example", globalBindings, localBindings, menu)

    def runExample(self, event):
        print("DEBUG: jonsor example ran.")

def createMode():
    return Example()