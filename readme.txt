# Computer Lab Management System

A lightweight Windows-based solution to secure and manage computer lab environments in educational institutions. The system automatically restores lab PCs to a predefined clean state upon every reboot and restricts unauthorized system changes. It is ideal for schools, training centers, and public access labs.

---

## Project Objective

To maintain consistent and clean system states across all student computers in the lab by:
- Preventing unauthorized installations or system modifications
- Automatically restoring the system on reboot
- Reducing administrative overhead and support time
- Enabling future central monitoring and control by the instructor

---

## Features

- Automatic system restoration after each reboot using a predefined image
- Local protection against:
  - Unwanted software installation
  - File transfers from external USB drives (except peripherals)
  - System modifications by non-admin users
- Scheduled or manual recovery using Macrium Reflect automation
- Lightweight client-side agent (`LabShield`)
- Designed for offline environments with no need for cloud services
- Modular design for future upgrades (e.g., centralized dashboard)

---

## Technologies Used

- **Batch scripting (.bat)** for automating system restoration
- **XML** for Macrium Reflect configuration
- **Python** (planned) for server-side dashboard logic
- **C#** for developing the `LabShield` Windows executable
- **Windows Task Scheduler** for automated execution

---

## Usage Instructions

1. Install `LabShield_Setup.exe` on each student computer.
2. Place the recovery image and scripts in a fixed path (e.g., `D:\reflect\`).
3. Use Task Scheduler to run `LabRestore.bat` at startup or shutdown.
4. Update the `.mrimg` image manually when needed, replacing the existing one in the same path.
5. (Optional) The system can be extended to respond to remote commands from the teacher’s PC.

---

## File Structure

ComputerLabSystem/
├── LabShield_Setup.exe # Lightweight agent installed on student PCs
├── Reflect.exe # Macrium Reflect command-line tool
├── restore.xml # XML config for automated restore
├── Win10LabImage.mrimg # System image file
├── LabRestore.bat # Script to trigger restore


---

## Completed Tasks

- Created initial lab system image with all required settings and software
- Configured Macrium Reflect automation for silent restore
- Developed and tested `LabRestore.bat` with task scheduler
- Built `LabShield` lightweight executable for local policy enforcement
- Verified local restore works after reboot without user interaction

---

## Tasks In Progress

- Developing a centralized dashboard for the teacher to:
  - Monitor lab device status
  - Send commands (restart, lock, restore)
- Adding USB monitoring and blocking within `LabShield`
- Creating a bundled EXE installer to simplify deployment on multiple machines
- Improving logging and error reporting for system restore operations

---

## Future Roadmap

- Optional LAN-based communication between client machines and teacher dashboard
- Support for additional OS versions (Windows 11 Education, Windows Server)
- Backup scheduling and incremental image updates
- Linux-based alternative for open-source environments

---

## License

This project is currently intended for internal use in educational institutions. Licensing terms will be finalized in future updates.

---

## Contributions

Suggestions, feature requests, and bug reports are welcome.  
Please open an issue or submit a pull request to contribute.
