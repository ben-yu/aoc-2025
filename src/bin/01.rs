advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u64> {
    let mut start_pos = 50;
    let mut password = 0;
    let circle_size = 100;

    for line in input.lines() {
        let mut op = String::from(line);
        let rot_size = op.split_off(1).parse::<i32>().unwrap();
        if op == "L" {
            start_pos = (start_pos - rot_size) % circle_size;
        } else if op == "R" {
            start_pos = (start_pos + rot_size) % circle_size;
        }
        if start_pos == 0 {
            password += 1;
        }
    }
    Some(password)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut start_pos = 50;
    let mut password = 0;
    let circle_size = 100;

    for line in input.lines() {
        let mut op = String::from(line);
        let mut rot_size = op.split_off(1).parse::<i32>().unwrap();

        let ini_pos = start_pos;

        password += rot_size / circle_size;
        rot_size %= circle_size;

        if rot_size == 0 {
            continue;
        }

        if op == "R" {
            start_pos += rot_size;
            if start_pos > (circle_size - 1) && ini_pos != 0 {
                password += 1;
            }
        } else if op == "L" {
            start_pos += circle_size;
            start_pos -= rot_size;
            if start_pos <= circle_size && ini_pos != 0 {
                password += 1;
            }
        }

        start_pos %= circle_size;
    }
    Some(password as u64)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(6));
    }
    #[test]
    fn test_large_rotation() {
        let result = part_two(&String::from("R1000"));
        assert_eq!(result, Some(10));
    }

}
