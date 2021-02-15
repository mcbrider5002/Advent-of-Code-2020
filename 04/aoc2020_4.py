with open("input.txt", 'r') as f:
    entries = [dict(pair.split(':') for pair in pport.replace("\n", " ").split(" ") if pair.strip() != "") for pport in f.read().split("\n\n")]
  
def validate(entry):
    try: byr, iyr, eyr, hgt, hcl, ecl, pid = entry["byr"], entry["iyr"], entry["eyr"], entry["hgt"], entry["hcl"], entry["ecl"], entry["pid"]
    except: return False, False
    return True, (
        len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002
        and len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020  
        and len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030
        and (hgt[-2:] == "cm" and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193  
            or hgt[-2:] == "in" and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76)
        and hcl[0] == "#" and all(d in map(str, range(10)) or d in ["a", "b", "c", "d", "e", "f"] for d in hcl[1:])
        and ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        and len(pid) == 9 and pid.isnumeric() 
    )

print(f"Pt1: {sum(validate(e)[0] for e in entries)}\nPt2: {sum(validate(e)[1] for e in entries)}")