
    document.addEventListener('DOMContentLoaded', function () {
        const checkboxes = document.querySelectorAll('.call-checkbox');
        const schoolList = document.querySelector('.school-list');

        // Load saved checkbox states from localStorage and reorder the list
        checkboxes.forEach(checkbox => {
            const index = checkbox.dataset.index;
            const savedState = localStorage.getItem(`checkbox-${index}`);

            const schoolItem = document.getElementById('school-' + index);

            if (savedState === 'checked') {
                checkbox.checked = true;
                schoolItem.classList.add('completed');
                schoolList.appendChild(schoolItem);  // Move to the end of the list
            }
        });

        // Add event listener for checkbox change
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function () {
                const schoolItem = document.getElementById('school-' + this.dataset.index);

                if (this.checked) {
                    // Move completed item to the end of the list and save the state
                    schoolItem.classList.add('completed');
                    schoolList.appendChild(schoolItem);
                    localStorage.setItem(`checkbox-${this.dataset.index}`, 'checked');
                } else {
                    // Move unchecked item back to the top and save the state
                    schoolItem.classList.remove('completed');
                    schoolList.insertBefore(schoolItem, schoolList.firstChild);
                    localStorage.setItem(`checkbox-${this.dataset.index}`, 'unchecked');
                }
            });
        });
    });
    