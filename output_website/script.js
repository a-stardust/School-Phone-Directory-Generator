
    document.addEventListener('DOMContentLoaded', function () {
        const checkboxes = document.querySelectorAll('.call-checkbox');

        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function () {
                const schoolItem = document.getElementById('school-' + this.dataset.index);
                const schoolList = document.querySelector('.school-list');

                if (this.checked) {
                    // Move completed item to the end of the list
                    schoolItem.classList.add('completed');
                    schoolList.appendChild(schoolItem);
                } else {
                    // Move unchecked item back to the top
                    schoolItem.classList.remove('completed');
                    schoolList.insertBefore(schoolItem, schoolList.firstChild);
                }
            });
        });
    });
    