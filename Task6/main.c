#include <stdio.h>
#include "ch32v00x.h"

void My_USART_Init(void) {
    RCC->APB2PCENR |= RCC_APB2Periph_USART1;  // Enable USART1
    RCC->APB2PCENR |= RCC_APB2Periph_GPIOD;   // Enable GPIO Port D

    GPIOD->CFGLR &= ~((0xF << 20) | (0xF << 24)); // Clear TX (PD5) and RX (PD6)
    GPIOD->CFGLR |= (0xB << 20) | (0x4 << 24);   // TX (PD5) Output 50MHz AF, RX (PD6) Input Floating

    USART_InitTypeDef USART_InitStructure;
    USART_InitStructure.USART_BaudRate = 115200;
    USART_InitStructure.USART_WordLength = USART_WordLength_8b;
    USART_InitStructure.USART_StopBits = USART_StopBits_1;
    USART_InitStructure.USART_Parity = USART_Parity_No;
    USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;

    USART_Init(USART1, &USART_InitStructure);
    USART_Cmd(USART1, ENABLE);
}

char USART_ReadChar(void) {
    while (!(USART1->STATR & USART_STATR_RXNE)); // Wait for data
    return USART1->DATAR;
}

void USART_WriteChar(char c) {
    while (!(USART1->STATR & USART_STATR_TXE)); // Wait until ready to send
    USART1->DATAR = c;
}

void USART_WriteString(const char *str) {
    while (*str) {
        USART_WriteChar(*str++);
    }
}

int main(void) {
    My_USART_Init();
    USART_WriteString("VSDSquadron Mini Ready\n");

    while (1) {
        char received = USART_ReadChar();
        USART_WriteChar(received); // Echo back
    }
}
