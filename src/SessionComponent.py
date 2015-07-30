# -*- coding: utf-8 -*-
from _Framework.Util import index_if
from _Framework.SessionComponent import SessionComponent as SessionComponentBase
from .SceneComponent import SceneComponent
from .Log import log_message

class SessionComponent(SessionComponentBase):
    _session_component_ends_initialisation = False
    scene_component_type = SceneComponent

    def __init__(self, *a, **k):
        super(SessionComponent, self).__init__(*a, **k)
        self.set_offsets(0, 0)
        self.on_selected_scene_changed()
        self.on_selected_track_changed()

    def on_selected_track_changed(self):
        all_tracks = self.tracks_to_use()
        selected_track = self.song().view.selected_track
        num_strips = self.width()
        if selected_track in all_tracks:
            track_index = list(all_tracks).index(selected_track)
            new_offset = track_index - track_index % num_strips
            self.set_offsets(new_offset, self.scene_offset())

    def on_selected_scene_changed(self):
        super(SessionComponent, self).on_selected_scene_changed()
        all_scenes = self.song().scenes
        selected_scene = self.song().view.selected_scene
        new_offset = index_if(lambda a: a == selected_scene, all_scenes)
        if new_offset < len(all_scenes):
            self.set_offsets(self.track_offset(), new_offset)

    def _enable_skinning(self):
        super(SessionComponent, self)._enable_skinning()
        # added for stop all button
        self.set_stop_all_on_value('Session.StopAllOn')
        self.set_stop_all_off_value('Session.StopAllOff')
        # added for CLipEmpty
        for scene_index in xrange(self._num_scenes):
            scene = self.scene(scene_index)
            for track_index in xrange(self._num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_empty_value('Session.ClipEmpty')
            
    def set_stop_all_on_value(self, value):
        self._stop_all_on_value = value
        
    def set_stop_all_off_value(self, value):
        self._stop_all_off_value = value
        
    def _update_stop_all_clips_button(self):
        button = self._stop_all_button
        button and button.set_light(self._stop_all_on_value if button.is_pressed() else self._stop_all_off_value)
