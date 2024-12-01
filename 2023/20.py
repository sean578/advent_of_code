"""
"""

if __name__ == '__main__':
    # flip-flop = %in -> out
    # conjunction = &
    # broadcaster (only one). Sends same pulse to all destinations.
    # button module # Not explicity in input. Sends a low pulse to broadcaster.

    configuration = [line.strip().split(" -> ") for line in open("20_debug.txt").readlines()]

    things = []
    all_inputs = []
    for config in configuration:
        print(config)
        thing, inputs = config
        inputs = inputs.split(", ")

        if "%" in thing:
            things.append(("flipflop", thing[1:]))
        elif "&" in thing:
            things.append(("conjunction", thing[1:]))
        else:
            assert thing == "broadcaster"
            things.append((thing, None))

        all_inputs.append(inputs)

    print()
    for thing, ins in zip(things, all_inputs):
        print(thing, ins)