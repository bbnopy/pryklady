def half(filename):
    source = makeSound(filename)
    target = makeSound(filename)

    sourceIndex = 1
    for targetIndex in range(1, getLength( target)+1):
        setSampleValueAt( target, targetIndex, getSampleValueAt(source, int(sourceIndex)))
        sourceIndex = sourceIndex + 0.5

        play(target)
        return target
