# Repo Aoi - Intelligent System Manager

> **Aoi** is an intelligent bot designed for hardware monitoring and automation using Python.

---


## 🗺️ Phase 1: The Control Station (Foundations)
> **Goal:** Build a bulletproof foundation for the bot's core logic. Chapter 1 has been expanded to 12 intensive modules.

    [x] Lesson 01: Variables, Data Types & F-strings

    [x] Lesson 02: System Pulse (time.sleep & while True)

    [x] Lesson 03: Decision Logic (if/elif/else)

    [x] Lesson 04: Power Packaging (def Functions)

    [x] Lesson 05: Exception Handling (try-except)

    [ ] Lesson 06: File I/O & JSON - Long-term Memory

    [ ] Lesson 07: Basic List & Dict - Alert Management

    [ ] Lesson 08: Advanced Parameters (*args, **kwargs)

    [ ] Lesson 09: Time Management (datetime)

    [ ] Lesson 10: OOP Basics - Entity Encapsulation

    [ ] Lesson 11: Basic Threading - Multi-tasking

    [ ] Lesson 12: System Logging - Audit Trail

---

## 🛠️ Dev Log & Daily Progress

### 🧱 Chapter 1: Foundations

> **Lesson 5**: Exception Handling (try-except) - Building Bulletproof Systems.

**Main File: research/chapter_01/05_lession/05_exception_handling.py**

```text
Key Technical Milestones:

- Data Integrity Protection: Implemented try-except blocks to intercept ValueError, ensuring the bot doesn't crash when receiving non-numeric inputs.

- Graceful Shutdowns: Integrated KeyboardInterrupt handling to manage manual system exits (Ctrl+C) with clean status messages.

- Zero-Failure Logic: Applied ZeroDivisionError prevention to handle critical calculation risks in energy distribution modules.

- Mandatory Cleanup Protocols: Utilized finally blocks to guarantee that system logs and "safe-state" messages are always executed, regardless of errors.
