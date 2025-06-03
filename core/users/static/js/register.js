function toggleFields() {
    const studentFields = document.getElementById('student-fields');
    const facultyFields = document.getElementById('faculty-fields');
    const role = roleField.value;

    // Enable & show relevant fields, disable others
    if (role === 'student') {
        studentFields.style.display = 'block';
        facultyFields.style.display = 'none';

        // Enable student inputs
        studentFields.querySelectorAll('input').forEach(el => el.disabled = false);
        // Disable faculty inputs
        facultyFields.querySelectorAll('input').forEach(el => el.disabled = true);
    }
    else if (role === 'faculty') {
        studentFields.style.display = 'none';
        facultyFields.style.display = 'block';

        facultyFields.querySelectorAll('input').forEach(el => el.disabled = false);
        studentFields.querySelectorAll('input').forEach(el => el.disabled = true);
    }
    else {
        studentFields.style.display = 'none';
        facultyFields.style.display = 'none';

        facultyFields.querySelectorAll('input').forEach(el => el.disabled = true);
        studentFields.querySelectorAll('input').forEach(el => el.disabled = true);
    }
}
