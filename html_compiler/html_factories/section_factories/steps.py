def build_first_step(subsections,
        absolute_path, relative_path, static_storage_absolute_path, compile_section):
    step_subbody_html = ''

    step_subbody_html += '<div class="first-step">'
    step_subbody_html += compile_section(subsections,
            absolute_path, relative_path, static_storage_absolute_path)
    step_subbody_html += '</div>'

    return step_subbody_html


def build_middle_steps(steps,
        absolute_path, relative_path, static_storage_absolute_path, compile_section):
    step_subbody_html = ''

    for subsections in steps:
        step_subbody_html += '<div class="middle-step">'
        step_subbody_html += compile_section(subsections,
                absolute_path, relative_path, static_storage_absolute_path)
        step_subbody_html += '</div>'

    return step_subbody_html


def build_last_step(subsections,
        absolute_path, relative_path, static_storage_absolute_path, compile_section):
    step_subbody_html = ''

    step_subbody_html += '<div class="last-step">'
    step_subbody_html += compile_section(subsections,
            absolute_path, relative_path, static_storage_absolute_path)
    step_subbody_html += '</div>'

    return step_subbody_html


class StepSectionFactory:
    @staticmethod
    def build_html(subsections,
            absolute_path, relative_path, static_storage_absolute_path, compile_section):
        step_body_html = ''

        step_body_html += build_first_step(subsections[0],
                absolute_path, relative_path, static_storage_absolute_path, compile_section)
        if subsections[1:-1]:
            step_body_html += build_middle_steps(subsections[1:-1],
                    absolute_path, relative_path, static_storage_absolute_path, compile_section)
        step_body_html += build_last_step(subsections[-1],
                absolute_path, relative_path, static_storage_absolute_path, compile_section)

        return step_body_html
