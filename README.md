# RISC-V Internship program powered by SAMSUNG and VSD
### This RISC-V Internship using VSDSquadron Mini is based on RISC-V architecture and uses open-source tools to teach students about VLSI SoC Design and RISC-V. The instructor and guide for this internship is Kunal Ghosh Sir, Founder of VSD.

##  Basic Details

**Name:** Amish Srinivasan S  
**College:** RV Institute of Technology and Management                                         
**Email ID:** srinivasanamish@gmail.com  
**GitHub Profile:** [metalyeager](https://github.com/metalyeager)  
**LinkedIN Profile:** [Amish Srinivasan S](https://www.linkedin.com/in/amish-srinivasan-528448298/)


# Task 1
<details>
<summary>C based Lab Screenshots</summary>
<br>
 
![WhatsApp Image 2025-01-06 at 23 46 13_907fca43](https://github.com/user-attachments/assets/10dd4878-caa1-4dea-829b-4790631abd14)
</details>
<details>
<summary>RISC-V based lab screenshots</summary>
<br>

![WhatsApp Image 2025-01-07 at 00 12 41_5a49a897](https://github.com/user-attachments/assets/6268329b-f886-4582-bee8-b68b192e2e1a)


</details>

# Task 2
<details>
<summary>Spike Simulation for the C program sum1ton.c and object dump's address allocation observation with calculations</summary>
<br>
  
![WhatsApp Image 2025-01-13 at 20 16 02_5119eabd](https://github.com/user-attachments/assets/c42f5b5c-d0b2-43f1-a712-e12052719eba)

![WhatsApp Image 2025-01-13 at 20 16 19_d92527c5](https://github.com/user-attachments/assets/fd848642-9feb-4b08-ab01-a2d76420bbe1)

![WhatsApp Image 2025-01-13 at 20 15 31_4924468d](https://github.com/user-attachments/assets/15519792-834f-4e38-8b3b-1276f36c0e45)

</details>
<details>
<summary>C based Lab Screenshots- Implementation of Fibonacci sequence upto 20 terms</summary>
<br>
  
  ![WhatsApp Image 2025-01-13 at 21 19 10_cece3c16](https://github.com/user-attachments/assets/78b3572c-e270-4ecc-886e-e2ef2528dee6)
</details>
<details>
<summary>RISC-V based lab screenshots for Spike Simulation of the C program fibo.c and Object dump's address allocation observations</summary>
<br>
  
#### Using -O1 compilation algorithm

![WhatsApp Image 2025-01-15 at 14 07 13_46162e79](https://github.com/user-attachments/assets/0dc6e7ed-e43c-435d-981d-08cfb325e9e9)
#### Using -Ofast compliation algorithm

![WhatsApp Image 2025-01-15 at 14 13 52_7dc94361](https://github.com/user-attachments/assets/4226492f-4eec-4740-b72d-e09f2e680537)

</details>

# Task 3
<details>
<summary></summary>
<br>

 ![Image](https://github.com/user-attachments/assets/3a30a7f2-4067-4784-a5a4-af0e47cf8d41)
 
Instruction 1
Instruction: lui a2, 0x1
Type: U-Type
Opcode: 0110111 (lui)
Destination Register: a2 = x12 → 01100
Immediate: 0x1 → 00000000000000000001 (20 bits)
Overall Encoding:
00000000000000000001 | 01100 | 0110111

Instruction 2
Instruction: lui a0, 0x21
Type: U-Type
Opcode: 0110111 (lui)
Destination Register: a0 = x10 → 01010
Immediate: 0x21 → 00000000000100001 (20 bits)
Overall Encoding:
00000000000100001 | 01010 | 0110111

Instruction 3
Instruction: addi sp, sp, -16
Type: I-Type
Opcode: 0010011 (addi)
Destination Register: sp = x2 → 00010
Source Register: sp = x2 → 00010
Immediate: -16 → 1111111111110000 (12 bits, sign-extended)
Overall Encoding:
1111111111110000 | 00010 | 000 | 00010 | 0010011

Instruction 4
Instruction: addi a2, a2, 954
Type: I-Type
Opcode: 0010011 (addi)
Destination Register: a2 = x12 → 01100
Source Register: a2 = x12 → 01100
Immediate: 954 → 0011101010 (12 bits, sign-extended)
Overall Encoding:
0011101010 | 01100 | 000 | 01100 | 0010011

Instruction 5
Instruction: addi a1, a1, 100
Type: I-Type
Opcode: 0010011 (addi)
Destination Register: a1 = x11 → 01011
Source Register: a1 = x11 → 01011
Immediate: 100 → 00000001100100 (12 bits, sign-extended)
Overall Encoding:
00000001100100 | 01011 | 000 | 01011 | 0010011

Instruction 6
Instruction: addi a0, a0, 384
Type: I-Type
Opcode: 0010011 (addi)
Destination Register: a0 = x10 → 01010
Source Register: a0 = x10 → 01010
Immediate: 384 → 00000110000000 (12 bits, sign-extended)
Overall Encoding:
00000110000000 | 01010 | 000 | 01010 | 0010011

Instruction 7
Instruction: sd ra, 8(sp)
Type: S-Type
Opcode: 0100011 (sd)
Source Register: ra = x1 → 00001
Base Register: sp = x2 → 00010
Immediate: 8 → 0000000001000 (split into imm[11:5] and imm[4:0])
Overall Encoding:
0000000 | 00001 | 00010 | 010 | 0001000 | 0100011

Instruction 8
Instruction: jal ra, 1040c
Type: J-Type
Opcode: 1101111 (jal)
Destination Register: ra = x1 → 00001
Offset: 1040c → 00010000000000001100 (20 bits, sign-extended)
Overall Encoding:
00010000000000001100 | 00001 | 1101111

Instruction 9
Instruction: ld ra, 8(sp)
Type: I-Type
Opcode: 0000011 (ld)
Destination Register: ra = x1 → 00001
Base Register: sp = x2 → 00010
Immediate: 8 → 0000000001000 (12 bits, sign-extended)
Overall Encoding:
0000000001000 | 00010 | 011 | 00001 | 0000011

Instruction 10
Instruction: addi a0, a0, 0
Type: I-Type
Opcode: 0010011 (addi)
Destination Register: a0 = x10 → 01010
Source Register: a0 = x10 → 01010
Immediate: 0 → 000000000000 (12 bits, sign-extended)
Overall Encoding:
000000000000 | 01010 | 000 | 01010 | 0010011

Instruction 11
Instruction: addi sp, sp, 16
Type: I-Type
Opcode: 0010011 (addi)
Destination Register: sp = x2 → 00010
Source Register: sp = x2 → 00010
Immediate: 16 → 00000000010000 (12 bits, sign-extended)
Overall Encoding:
00000000010000 | 00010 | 000 | 00010 | 0010011

Instruction 12
Instruction: ret
Type: I-Type (jalr)
Opcode: 1100111 (jalr)
Destination Register: x0 → 00000
Base Register: ra = x1 → 00001
Immediate: 0 → 000000000000 (12 bits, sign-extended)
Overall Encoding:
000000000000 | 00001 | 000 | 00000 | 1100111
</details>
<details>
<summary>RISC-V based lab screenshots</summary>
<br>

![WhatsApp Image 2025-01-07 at 00 12 41_5a49a897](https://github.com/user-attachments/assets/6268329b-f886-4582-bee8-b68b192e2e1a)


</details>
