# **Python Text Calculator**
This calculator provides a lot of the normal functionality that you would expect from a calculator. To start the calculator you will want to go to open a terminal window and locate to this directory. Next run the following commands:
```console
$ python path/to/src/main.py
```
In the calculator there is an easy way for you to access help for functions:
```
: help (optional: page number or function)
```
## Example Commands
#### Addition #1
```py
: 3
```
```py
: +
```
```py
: 3
```
#### Addition #2
```py
: 3
```
```py
: + 3
```
#### Addition #3
```py
: 3 +
```
```py
: 3
```
#### Addition #4
```py
: 3 + 3
```
All the above are valid commands, not only for addition. The operator can be replaced with whichever other operations are available. Check out `help` for more information on the available commands.
## Addition Info
These calculator commands are exectued from left to right, so you may enter a long string of numbers and operators, separated by spaces, to receive an answer.
#### *Example*
```py
: 13 + 4 - 15 * 16 ** 3 / 5 - 25
```
One thing you may notice after executing this is that it does not follow the rules of order of operations.

<table>
    <tr>
        <th>Expected Answer</th>
        <th>Resulted Answer</th>
    </tr>
    <td><samp>-12296</td>
    <td><samp>6528.6</td>
</table>

Unfortunately, this calculator does not use order of operations in its calculations, however, this may be implemented in the future, so stay tuned.

## Calculator Funtions
If you don't to go through the help function of the calculator, here is a list of all the possible commands. You can specifically look up what they do in the help function of the calculator.
* help
* settings
* off
* clear
* reset
* (number)
* e
* pi
* add
* subtract
* multiple
* divide
* power
* sqrt
* root
* factorial
* sin
* cos
* tan
* ln
* log
* mode
* show/hide help/poweroff msg