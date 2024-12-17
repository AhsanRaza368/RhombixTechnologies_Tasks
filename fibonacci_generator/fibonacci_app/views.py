from django.shortcuts import render

def fibonacci_view(request):
    sequence = []
    if request.method == "POST":
        try:
            n = int(request.POST.get("number"))
            if n >= 1:
                sequence = [0, 1] if n > 1 else [0]
                while len(sequence) < n:
                    sequence.append(sequence[-1] + sequence[-2])
            else:
                sequence = ["Input must be greater than 0"]
        except ValueError:
            sequence = ["Please enter a valid number"]
    return render(request, "fibonacci_app/fibonacci.html", {"sequence": sequence})
