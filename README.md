# Smart-Car-Management-System (SCMS)

## Introduction

Changing tires with conventional jacks poses difficulties for many individuals, particularly the elderly, and can be especially challenging in adverse weather conditions. These jacks require the operator to remain in a bent over or squatting position, which is not ergonomic and may lead to discomfort or injury. Additionally, the safety features of current jacks are often inadequate, and their size and weight make them difficult to store, transport, or position.

SCMS aims to address these issues by providing an electric car jack system that is powered by the car's battery and uses IoT and Smart Automation technologies. This system allows the operator to initiate the tire-changing process with the simple push of a button on a Graphical User Interface (GUI), significantly reducing hassle and improving safety.

## Project Overview

- **Smart Control**: The jack's movement is controlled by a Programmable Logic Controller (PLC), which integrates data from the Tyre Pressure Monitoring System (TPMS) and user input from an HMI and GUI.
- **Real-Time Monitoring**: The system continuously checks tire pressure, and if a tire is detected to be low or flat, it informs the user via the HMI.
- **User Interaction**: Upon a flat tire warning, the user can initiate the lifting process by pressing the "Start Button". After tire replacement, pressing the "Complete Button" retracts the jack to its original position.
- **Automation**: The PLC controls the horizontal and vertical movement of the jack based on the input received and ensures the jack is retracted after the process.

## Detailed Working

- **Monitoring**: The system constantly checks the pressure of all tires.
- **Interrupt Handling**: If the TPMS detects low pressure or a flat tire, it generates an interrupt that the controller processes.
- **User Guidance**: The HMI displays continuous warnings for low pressure and emergency messages for flat tires.
- **Activation**: On user confirmation, the jack placement process begins to hoist the vehicle.
- **Placement and Lifting**: The PLC guides the jack to the correct position and raises the car to the required height.
- **Replacement and Retraction**: After the tire is replaced and the user confirms completion, the jack is folded and retracted.
- **Safety Checks**: The system runs a final confirmation test to ensure all parameters are correct.

## Features & Outcomes

- **Innovative and Smart**: Incorporates IoT for a smarter approach to tire changing.
- **User-Friendly**: Features an intuitive Graphical User Interface for easy operation.
- **Safety-Enhancing**: Reduces accidents related to tire changes and improves safety for women and the elderly.
- **Efficient**: Offers real-time tire pressure data, saves time and effort.
- **Convenient**: Hassle-free operation with minimal physical effort required.

## How to Use

1. **Start**: When notified of a flat tire, press the "Start Button" on the GUI.
2. **Replace Tire**: After the car is hoisted, replace the deflated tire with a spare.
3. **Complete**: Press the "Complete Button" to retract the jack and lower the car.


## Conclusion

SCMS provides an ergonomic, safe, and smart solution to changing tires, making it a valuable tool for car owners and operators who seek convenience and safety in vehicle maintenance.

# Research Paper : https://link.springer.com/chapter/10.1007/978-981-15-5827-6_29
