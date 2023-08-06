{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN7N4cPXr8rPy40XxLc9hEz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MeenalJy/PyWarrior-Challenge/blob/main/partone.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Ask for the user’s first name and\n",
        "display the output message.\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "_EGkSekbH81e"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gSwqT4jGHSb-",
        "outputId": "592786c9-bf3b-4ac9-efdf-b460cf7e5280"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Jayant\n",
            "Hello Jayant\n"
          ]
        }
      ],
      "source": [
        "name = str(input(\"Enter your name: \"))\n",
        "\n",
        "print(\"Hello\", name)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Ask for the user’s first name and then ask for\n",
        "their surname and display the output message."
      ],
      "metadata": {
        "id": "6x1A_MowIb9d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "first_name = str(input(\"Enter your first name: \"))\n",
        "\n",
        "last_name = str(input(\"Enter your surname: \"))\n",
        "\n",
        "print(\"Hello\", first_name , last_name, \"Welcome to the club\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PyUCtXRnIjG1",
        "outputId": "64b2e6fc-df8b-464a-8289-efb531c28ced"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your first name: Mojo\n",
            "Enter your surname: Jojo\n",
            "Hello Mojo Jojo Welcome to the club\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Write code that will display the joke “What do you call a bear with no\n",
        "teeth?” and on the next line display the answer “A gummy bear!” Try to\n",
        "create it using only one line of code."
      ],
      "metadata": {
        "id": "-PAnwjr3JLK-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"What do you call a bear with no teeth? \\n \\nA gummy bear\")"
      ],
      "metadata": {
        "id": "2lEGYfZPJT0Y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a54a91f4-b6a8-4871-dedc-bfc865636fdd"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What do you call a bear with no teeth? \n",
            " \n",
            "A gummy bear\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Ask the user to enter\n",
        "two numbers. Add\n",
        "them together and\n",
        "display the answer as"
      ],
      "metadata": {
        "id": "QULG9ljmDH9I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num_1 = float(input(\"Enter the first number:\"))\n",
        "\n",
        "num_2 = float(input(\"Enter your second number: \"))\n",
        "\n",
        "sum = num_1 + num_2\n",
        "\n",
        "print(\"The sum of the two numbers is: \", sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wAOvuoIiDjNE",
        "outputId": "880cea62-539d-4a92-d1c0-2a94e3273f13"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number:23\n",
            "Enter your second number: 24\n",
            "The sum of the two numbers is:  47.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Ask the user to enter three\n",
        "numbers. Add together the first\n",
        "two numbers and then multiply\n",
        "this total by the third. Display the\n",
        "answer as The answer is"
      ],
      "metadata": {
        "id": "tyCnH8mUD-GP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num_1 = float(input(\"Enter the first number: \"))\n",
        "\n",
        "num_2 = float(input(\"Enter the second number: \"))\n",
        "\n",
        "num_3 = float(input(\"Enter the third number: \"))\n",
        "\n",
        "sum = ((num_1) + (num_2)) * (num_3)\n",
        "print(\"The answer is \", sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5dUZYaoREK12",
        "outputId": "701a5599-741c-42c0-9dac-ba270f305550"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number: 5\n",
            "Enter the second number: 100\n",
            "Enter the third number: 1000\n",
            "The answer is  105000.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. Ask how many slices\n",
        "of pizza the user\n",
        "started with and ask\n",
        "how many slices\n",
        "they have eaten.\n",
        "Work out how many\n",
        "slices they have left\n",
        "and display the\n",
        "answer in a userfriendly\n",
        "format."
      ],
      "metadata": {
        "id": "FynWFWBtFZQB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total_slice = int(input(\"The number of pizza slices in total: \"))\n",
        "eaten_slice = int(input(\"The number of pizza slices you have eaten: \"))\n",
        "diff = ((total_slice) - (eaten_slice))\n",
        "\n",
        "print(\"Number of pizza slices are left: \", diff)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0e74cf84-231f-48bb-e170-7a4415cc8efe",
        "id": "cSRr7PyHHSdt"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The number of pizza slices in total: 50\n",
            "The number of pizza slices you have eaten: 35\n",
            "Number of pizza slices are left:  15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. Ask the user for their name and their age. Add 1 to their age\n",
        "and display the output"
      ],
      "metadata": {
        "id": "b2g25p5LH-a4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name_friend = str(input(\"Enter your name: \"))\n",
        "\n",
        "age_friend = int(input(\"Enter your age: \"))\n",
        "\n",
        "birthday = (age_friend) + 1\n",
        "\n",
        "print(\"Hello,\", (name_friend), \"on your next birthday you will be \", birthday)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5hLSwuroIKhI",
        "outputId": "18a9c3b1-b13a-49c6-e7a0-dd0342773f47"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Muskaan\n",
            "Enter your age: 21\n",
            "Hello, Muskaan on your next birthday you will be  22\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. Ask for the total price of the bill, then ask how\n",
        "many diners there are. Divide the total bill by the\n",
        "number of diners and show how much each\n",
        "person must pay."
      ],
      "metadata": {
        "id": "IbFegS6iI9FF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "bill_total = float(input(\"Enter the total bill: \"))\n",
        "\n",
        "num_diners = int(input(\"Enter total number of diners: \"))\n",
        "\n",
        "each_diner = ((bill_total) / (num_diners))\n",
        "\n",
        "print(\"Each person has to pay Rupees \",each_diner)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "26HpoReMJCV4",
        "outputId": "37955522-2f75-4e02-b9d1-bfab260e3e49"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the total bill: 200\n",
            "Enter total number of diners: 4\n",
            "Each person has to pay Rupees  50.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9. Write a program\n",
        "that will ask for a\n",
        "number of days\n",
        "and then will\n",
        "show how many\n",
        "hours, minutes\n",
        "and seconds are\n",
        "in that number"
      ],
      "metadata": {
        "id": "eunmA-FdKIOQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num_of_days = int(input(\"Enter the number of days: \"))\n",
        "\n",
        "num_of_hr = int((num_of_days) * 24 )\n",
        "num_of_min = int((num_of_hr) * 60 )\n",
        "num_of_secs = int((num_of_min) * 60)\n",
        "print(\"In\", (num_of_days), \"days, total hours are \",(num_of_hr), \"\\ntotal minutes are \",(num_of_min), \"\\ntotal seconds are \", (num_of_secs) )\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DbSgHWDNKN7w",
        "outputId": "7f3d00c0-d860-4f94-9b76-3ddafbc7b756"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of days: 1\n",
            "In 1 days, total hours are  24 \n",
            "total minutes are  1440 \n",
            "total seconds are  86400\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "10. There are 2,204 pounds in a kilogram. Ask the\n",
        "user to enter a weight in kilograms and convert it\n",
        "to pounds."
      ],
      "metadata": {
        "id": "3GZW2wjVOb6Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weight_of_user = float(input(\"Enter your weight in kg: \"))\n",
        "\n",
        "k_weight = float((weight_of_user) * 2204)\n",
        "\n",
        "p_weight = float((k_weight) / 1000)\n",
        "\n",
        "print(\"Your weight is \", (p_weight),\"pounds\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GCgDZxzpOhUv",
        "outputId": "d7ab1fbb-e0fb-43a2-9998-5c8cb1115593"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your weight in kg: 50\n",
            "Your weight is  110.2 pounds\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "11. Task the user to enter a number over 100 and then enter a number under\n",
        "10 and tell them how many times the smaller number goes into the larger\n",
        "number in a user-friendly format."
      ],
      "metadata": {
        "id": "_NgT8M09Qw4y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num_1 = float(input(\"Enter the number over 100: \"))\n",
        "\n",
        "num_2 = float(input(\"Enter the number smaller than 10: \"))\n",
        "\n",
        "inside = int((num_1) // (num_2))\n",
        "\n",
        "print(\"The number of times the smaller number goes into the larger number is: \", [inside])\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lIdLHxuTRpjw",
        "outputId": "8cbd01dd-4e20-481f-bd8d-2ce7f66eb121"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number over 100: 300\n",
            "Enter the number smaller than 10: 6\n",
            "The number of times the smaller number goes into the larger number is:  [50]\n"
          ]
        }
      ]
    }
  ]
}