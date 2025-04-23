try:
    name = input("📄 Enter filename: ")
    with open(name, 'r') as f:
        content = f.read().upper()  # 🔠 Make it shout!
    with open("modified_" + name, 'w') as out:
        out.write(content)
    print("✅ Done! Modified file saved.")
except FileNotFoundError:
    print("❌ File not found. Check the name and try again.")
except IOError:
    print("⚠️ Can't read the file. Permission or format issue?")
