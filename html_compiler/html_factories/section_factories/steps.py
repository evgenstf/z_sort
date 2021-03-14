def build_first_step(subsections, article_url, compile_sections):
    step_subbody_html = ''

    step_subbody_html += '<div class="first-step">'
    step_subbody_html += '<div class="step_number">'
    step_subbody_html += '1'
    step_subbody_html += '</div>'
    if not (subsections[0]['type'] == 'markdown' and subsections[0]['content'][
        0] == '#'):
        step_subbody_html += '<h1></h1>'
    step_subbody_html += '<div class="step_content">'
    step_subbody_html += compile_sections(article_url, subsections)
    step_subbody_html += '</div>'
    step_subbody_html += '</div>'

    return step_subbody_html


def build_middle_steps(subsections, article_url, compile_sections):
    step_subbody_html = ''

    for num_step, subsections in enumerate(steps):
        if num_step % 2 != 0:
            step_subbody_html += '<div class="middle-step">'
        else:
            step_subbody_html += '<div class="middle-step-colorized">'
        step_subbody_html += '<div class="step_number">'
        step_subbody_html += str(num_step + 2)
        step_subbody_html += '</div>'
        if not (subsections[0]['type'] == 'markdown' and subsections[0]['content'][0] == '#'):
            step_subbody_html += '<h1></h1>'
        step_subbody_html += '<div class="step_content">'
        step_subbody_html += compile_sections(article_url, subsections)
        step_subbody_html += '</div>'
        step_subbody_html += '</div>'

    return step_subbody_html


def build_last_step(subsections, subsections_length, article_url, compile_sections):
    step_subbody_html = ''

    if subsections_length % 2 != 0:
        step_subbody_html += '<div class="last-step">'
    else:
        step_subbody_html += '<div class="last-step-colorized">'
    step_subbody_html += '<div class="step_number">'
    step_subbody_html += str(subsections_length)
    step_subbody_html += '</div>'
    if not (subsections[0]['type'] == 'markdown' and subsections[0]['content'][
        0] == '#'):
        step_subbody_html += '<h1></h1>'
    step_subbody_html += '<div class="step_content">'
    step_subbody_html += compile_sections(article_url, subsections)
    step_subbody_html += '</div>'
    step_subbody_html += '</div>'

    return step_subbody_html


class StepSectionFactory:
    @staticmethod
    def build_html(subsections, article_url, compile_sections):
        step_body_html = ''
        if type(subsections) == str:
            import json
            subsections = json.loads(' '.join(str(subsections).split(' ')))
        step_body_html += build_first_step(subsections[0], article_url, compile_sections)
        if subsections[1:-1]:
            step_body_html += build_middle_steps(subsections[1:-1], article_url, compile_sections)
        step_body_html += build_last_step(subsections[-1], len(subsections), article_url, compile_sections)

        return step_body_html
