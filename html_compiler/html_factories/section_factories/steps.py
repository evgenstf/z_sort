class Step:
    @staticmethod
    def build_first_step(subsection, absolute_path, relative_path, static_storage_absolute_path, compile_section):

        step_subbody_html = ''

        with open("/home/leoproko/z_sort/z_sort/html_compiler/html_factories/section_factories/step_static/step_style.html", "r") as step_style:
            for line in step_style:
                step_subbody_html += line.strip()

        step_subbody_html += '<div class="first-step">'
        step_subbody_html += compile_section([subsection], absolute_path, relative_path, static_storage_absolute_path)
        step_subbody_html += '</div>'

        return step_subbody_html


    @staticmethod
    def build_middle_step(subsections, absolute_path, relative_path, static_storage_absolute_path, compile_section):

        step_subbody_html = ''

        for subsection in subsections[1:-1]:
            step_subbody_html += '<div class="middle-step">'
            step_subbody_html += compile_section([subsection], absolute_path, relative_path, static_storage_absolute_path)
            step_subbody_html += '</div>'

        return step_subbody_html



    @staticmethod
    def build_last_step(subsection, absolute_path, relative_path, static_storage_absolute_path, compile_section):

        step_subbody_html = ''

        step_subbody_html += '<div class="last-step">'
        step_subbody_html += compile_section([subsection], absolute_path, relative_path, static_storage_absolute_path)
        step_subbody_html += '</div>'

        return step_subbody_html



class StepSectionFactory:
    @staticmethod
    def build_html(subsections, absolute_path, relative_path, static_storage_absolute_path, compile_section):
        step_body_html = ''

        step_body_html += Step.build_first_step(subsections[0], absolute_path, relative_path, static_storage_absolute_path, compile_section)

        step_body_html += Step.build_middle_step(subsections, absolute_path, relative_path, static_storage_absolute_path, compile_section)

        step_body_html += Step.build_last_step(subsections[-1], absolute_path, relative_path, static_storage_absolute_path, compile_section)

        return step_body_html
