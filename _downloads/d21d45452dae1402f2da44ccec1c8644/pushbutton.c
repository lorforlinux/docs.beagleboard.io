////////////////////////////////////////
//	pushbutton.c
//      Reads P9_42 and prints its value.
//	Wiring:	Connect a switch between P9_42 and 3.3V
//	Setup:	
//	See:	
////////////////////////////////////////
#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#define CONSUMER        "pushbutton.c"

int main(int argc, char **argv)
{
        int chipnumber = 0;
        unsigned int line_num = 7;
        struct gpiod_line *line;
        struct gpiod_chip *chip;
        int i, ret;

        chip = gpiod_chip_open_by_number(chipnumber);
        line = gpiod_chip_get_line(chip, line_num);
        ret = gpiod_line_request_input(line, CONSUMER);

        /* Get */
        while(1) {
                printf("%d\r", gpiod_line_get_value(line));
                usleep(100);
        }
}
