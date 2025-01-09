## AUTHOR: WILLIAM PONCZAK
## DATE: 1/8/25
## VERSION: 1.0


import csv
from bs4 import BeautifulSoup
import pytest
from Schedule.course_scraper import extract_course_title, get_next_page_url, update_CSV


def test_extract_course_title():
    # Mock HTML
    mock_html = """ <html>
        <td class="width">
            <a href="preview_course_nopop.php?catoid=54&amp;coid=287862" target="_blank" title="ACTG 410. Auditing and Assurance   opens a new window" aria-expanded="false" onclick="showCourse('54', '287862',this, 'a:2:{s:8:~location~;s:8:~template~;s:28:~course_program_display_field~;i:1;}'); return false;">ACTG 410. Auditing and Assurance  </a>
        </td>
        <td class="width">
            <a href="preview_course_nopop.php?catoid=54&amp;coid=287961" target="_blank" title="ANTH 319. Human Osteology   opens a new window" aria-expanded="false" onclick="showCourse('54', '287961',this, 'a:2:{s:8:~location~;s:8:~template~;s:28:~course_program_display_field~;i:1;}'); return false;">ANTH 319. Human Osteology  </a>
        </td>
    </html>
    """
    
    soup = BeautifulSoup(mock_html, 'html.parser')
    tds = soup.find_all('td')

    titles = extract_course_title(tds)
    assert "ACTG 410. Auditing and Assurance" in titles
    assert "ANTH 319. Human Osteology" in titles

def test_get_next_page_url():
    import Schedule.course_scraper
    Schedule.course_scraper.count = 1

    url = get_next_page_url()
    assert url.endswith("filter%5Bcpage%5D=2#acalog_template_course_filter")

def test_update_CSV(tmp_path):
    #Dummy data
    data = [['CS101'], ['CS102']]
    from_filename = tmp_path / "from_file.csv"
    to_filename = tmp_path / "to_file.csv"

    #Write data to file
    with open(from_filename, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    #Call function and check output
    update_CSV(from_filename, to_filename)
    assert to_filename.exists()
    with open(to_filename, 'r') as f:
        lines = f.readlines()
    assert len(lines) == len(data)
    