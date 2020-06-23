def look_n_say_iterative(input_count):
    if input_count == 1:
        return "1"

    if input_count == 2:
        return "11"

    result = "11"
    for index in range(2, input_count):
        count = 1
        output = ""

        for i in range(1, len(result)):
            if result[i] != result[i - 1]:
                output = output + str(count) + result[i - 1]
                count = 1
            else:
                count = count + 1

            # if element is in last
            if i == len(result) - 1:
                output = output + str(count) + result[i]

        result = output
    return result


input_count = 6
result = look_n_say_iterative(input_count)
print(result)


def look_n_say_recursion(input_count):
    if input_count == 1:
        return "1"

    if input_count == 2:
        return "11"

    result = look_n_say_recursion(input_count - 1)
    count = 1
    output = ""

    for i in range(1, len(result)):
        if result[i] != result[i - 1]:
            output = output + str(count) + result[i - 1]
            count = 1
        else:
            count = count + 1

        # if element is in last
        if i == len(result) - 1:
            output = output + str(count) + result[i]
    return output


input_count = 6
result = look_n_say_recursion(input_count)
print(result)
